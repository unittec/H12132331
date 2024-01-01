from PyQt5.QtCore import QObject, pyqtSignal


class TreeModel(QObject):
    """ 树形结构模型 最大支持5层 """
    listViewModelChanged = pyqtSignal(list)

    def __init__(self):
        super().__init__()

        # 用于列表视图模型 二维列表 每一维对应一行节点，每个节点包含三个元素，第一个元素为节点深度，第二个元素为节点名称，第三个元素为是否显示状态，深度为0的节点为根节点，每个维度下标即为行号
        self._listViewModel = [[0, 123, True], [1, '子节点', True]]
        # 生成50个节点
        for i in range(0, 10):
            self._listViewModel.append([0, '根节点' + str(i), True])
            for j in range(0, 10):
                self._listViewModel.append([1, '子节点' + str(i) + '_' + str(j), True])
                for k in range(0, 10):
                    self._listViewModel.append([2, '子节点' + str(i) + '_' + str(j) + '_' + str(k), True])
                    for l in range(0, 10):
                        self._listViewModel.append(
                            [3, '子节点' + str(i) + '_' + str(j) + '_' + str(k) + '_' + str(l), True])

    @Property(list, notify=listViewModelChanged)
    def listViewModel(self):
        return self._listViewModel

    # 新增子节点
    @Slot(int, str, result=bool)
    def addChildNode(self, curr_row, new_node_name):
        """
        新增子节点
        :param curr_row: 当前节点行号
        :param new_node_name: 新节点名称
        :return: True 新增成功 False 新增失败
        """
        # 获取当前节点深度
        curr_depth = self._listViewModel[curr_row][0]
        # 如果存在子节点 找到末尾节点行号，追加节点 如果不存在则插入节点
        if self.has_children(curr_depth, curr_row):
            print('存在子节点')
            # 当前节点存在子节点，则检查子节点中是否有同名节点
            for row in range(curr_row + 1, len(self._listViewModel)):
                if self._listViewModel[row][0] <= curr_depth:
                    break
                if self._listViewModel[row][1] == new_node_name:
                    return False
            # 找到末尾节点行号
            while True:
                curr_row += 1
                if curr_row >= len(self._listViewModel):
                    break
                if self._listViewModel[curr_row][0] <= curr_depth:
                    break
            # 追加节点
            self._listViewModel.insert(curr_row, [curr_depth + 1, new_node_name, True])
        else:
            print('不存在子节点')
            # 插入前判断在当前节点下是否有同名节点
            for row in range(curr_row + 1, len(self._listViewModel)):
                if self._listViewModel[row][0] <= curr_depth:
                    break
                if self._listViewModel[row][1] == new_node_name:
                    return False
            # 插入节点
            self._listViewModel.insert(curr_row + 1, [curr_depth + 1, new_node_name, True])
        self.listViewModelChanged.emit(self._listViewModel)
        return True

    @Slot(str, result=bool)
    def addRootNode(self, new_node_name):
        """
        新增根节点
        :param new_node_name: 新节点名称
        :return: True 新增成功 False 新增失败
        """
        # 检查新名称是否在根节点中存在
        for row in self._listViewModel:
            if row[0] == 0 and row[1] == new_node_name:
                return False
        # 插入节点
        self._listViewModel.append([0, new_node_name, True])
        self.listViewModelChanged.emit(self._listViewModel)
        return True

    @Slot(int)
    def remove_node(self, curr_row):
        """
        删除节点 如节点有子节点则一并删除
        :param curr_row: 当前节点行号
        :return: None
        """
        # 获取当前节点深度
        curr_depth = self._listViewModel[curr_row][0]
        # 删除当前节点
        self._listViewModel.pop(curr_row)
        # 删除当前节点的子节点
        while True:
            if curr_row >= len(self._listViewModel):
                break
            if self._listViewModel[curr_row][0] <= curr_depth:
                break
            self._listViewModel.pop(curr_row)
        self.listViewModelChanged.emit(self._listViewModel)

    @Slot(int, int)
    def collapse_node(self, curr_depth, curr_row):
        """
        收起节点
        :param curr_depth: 当前节点深度
        :param curr_row: 当前节点行号
        :return: None
        """
        print('收起', curr_depth, curr_row)
        # 修改当前节点状态
        # self._listViewModel[curr_row][2] = False
        # 收起当前节点的子节点
        curr_row += 1
        if curr_row >= len(self._listViewModel):
            return
        while True:
            if curr_row >= len(self._listViewModel):
                break
            if self._listViewModel[curr_row][0] <= curr_depth:
                break
            self._listViewModel[curr_row][2] = False
            curr_row += 1
        self.listViewModelChanged.emit(self._listViewModel)

    @Slot(int, int)
    def expand_node(self, curr_depth, curr_row):
        """
        展开节点
        :param curr_depth: 当前节点深度
        :param curr_row: 当前节点行号
        :return: None
        """
        print('展开', curr_depth, curr_row)
        # 展开当前节点的子节点
        curr_row += 1
        while True:
            if curr_row >= len(self._listViewModel):
                break
            if self._listViewModel[curr_row][0] <= curr_depth:
                break
            self._listViewModel[curr_row][2] = True
            curr_row += 1
        self.listViewModelChanged.emit(self._listViewModel)

    @Slot(int, int, result=bool)
    def has_children(self, curr_depth, curr_row):
        """
        判断是否有子节点
        :param curr_depth: 当前节点深度
        :param curr_row: 当前节点行号
        :return: 是否有子节点
        """
        # print('has_children', curr_depth, curr_row)
        # 判断是否有子节点
        curr_row += 1
        while True:
            if curr_row >= len(self._listViewModel):
                break
            if self._listViewModel[curr_row][0] <= curr_depth:
                break
            if self._listViewModel[curr_row][0] == curr_depth + 1:
                return True
            curr_row += 1
        return False

    @Slot(int, int, result=bool)
    def get_child_display_status(self, curr_depth, curr_row):
        """
        获取子节点显示状态
        :param curr_depth: 当前节点深度
        :param curr_row: 当前节点行号
        :return: 子节点显示状态
        """
        # print('get_child_display_status', curr_depth, curr_row)
        # 判断是否有子节点
        curr_row += 1
        while True:
            if curr_row >= len(self._listViewModel):
                break
            if self._listViewModel[curr_row][0] <= curr_depth:
                break
            if self._listViewModel[curr_row][0] == curr_depth + 1:
                return self._listViewModel[curr_row][2]
            curr_row += 1
        return False

    @Slot(int, str, result=str)
    def set_node_name(self, curr_row, new_node_name):
        """
        设置节点名称
        :param curr_row:  当前节点行号
        :param new_node_name:  新节点名称
        :return: None
        """
        self._listViewModel[curr_row][1] = new_node_name
        self.listViewModelChanged.emit(self._listViewModel)
        return new_node_name

    @Slot(int, str, result=bool)
    def check_name(self, curr_row, new_node_name):
        """
        检查节点名称是否重复
        :param curr_row: 当前节点行号
        :param new_node_name: 新节点名称
        :return: True 不重复 False 重复
        """
        # 获取当前行深度
        curr_depth = self._listViewModel[curr_row][0]
        # 向前找 同级节点检查名称 更深级别节点不检查 遇到更浅级别节点则停止
        for row in range(curr_row - 1, -1, -1):
            if self._listViewModel[row][0] < curr_depth:
                break
            if self._listViewModel[row][0] == curr_depth and self._listViewModel[row][1] == new_node_name:
                return False
        # 向后找 同级节点检查名称 更深级别节点不检查 遇到更浅级别节点则停止
        for row in range(curr_row + 1, len(self._listViewModel)):
            if self._listViewModel[row][0] < curr_depth:
                break
            if self._listViewModel[row][0] == curr_depth and self._listViewModel[row][1] == new_node_name:
                return False
        return True

    def set_dict(self, dic):
        """
        根据字典生成树形结构
        :param dic: 字典
        :return: None
        """
        def get_tree(_curr_depth, _dic):
            """DFS递归生成树形结构"""
            for key, value in _dic.items():
                # 添加节点
                self._listViewModel.append([_curr_depth, key, True])
                # 判断是否有子节点
                if isinstance(value, dict):
                    # 递归
                    get_tree(_curr_depth + 1, value)
        # 清空数据
        self._listViewModel = []
        # 生成树形结构
        get_tree(0, dic)

    def get_dict(self):
        """
        获取树形结构字典 最大支持5层
        :return: 字典
        """
        tree_dict = {}
        for row in self._listViewModel:
            if row[0] == 0:
                tree_dict[row[1]] = {}
            elif row[0] == 1:
                tree_dict[list(tree_dict.keys())[-1]][row[1]] = {}
            elif row[0] == 2:
                tree_dict[list(tree_dict.keys())[-1]][list(tree_dict[list(tree_dict.keys())[-1]].keys())[-1]][row[1]] = {}
            elif row[0] == 3:
                tree_dict[list(tree_dict.keys())[-1]][list(tree_dict[list(tree_dict.keys())[-1]].keys())[-1]][
                    list(tree_dict[list(tree_dict.keys())[-1]][list(tree_dict[list(tree_dict.keys())[-1]].keys())[-1]].keys())[-1]][
                    row[1]] = {}
            elif row[0] == 4:
                tree_dict[list(tree_dict.keys())[-1]][list(tree_dict[list(tree_dict.keys())[-1]].keys())[-1]][
                    list(tree_dict[list(tree_dict.keys())[-1]][list(tree_dict[list(tree_dict.keys())[-1]].keys())[-1]].keys())[-1]][
                    list(tree_dict[list(tree_dict.keys())[-1]][list(tree_dict[list(tree_dict.keys())[-1]].keys())[-1]][
                             list(tree_dict[list(tree_dict.keys())[-1]][list(tree_dict[list(tree_dict.keys())[-1]].keys())[-1]].keys())[-1]].keys())[-1]][
                    row[1]] = {}
        return tree_dict

    def _find_key_at_depth(self, dictionary, target_depth, current_depth=0):
        """
        找到指定深度的所有key
        :param dictionary: 字典
        :param target_depth: 目标深度
        :param current_depth: 当前深度
        :return: None
        """
        for key, value in dictionary.items():
            if current_depth == target_depth:
                # print(f'Key at depth {target_depth}: {key}')
                ...
            elif isinstance(value, dict):
                self._find_key_at_depth(value, target_depth, current_depth + 1)
