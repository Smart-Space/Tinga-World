from typing import Union
#winui3
#部分组件无法展示

class TinUILight():
    '''
    这是TinUI明亮模式的托管类，不是继承类
    调用时这需要注意文本和数据，样式类参数无需理会
    '''

    def __init__(self,ui):
        super().__init__(ui,'tinui-light-theme')
        self.label='light'

    def add_button(self,pos,*arg,**kw):
        return self.ui.add_button(pos,fg='#1b1b1b',bg='#fbfbfb',
             activefg='#1a1a1a',activebg='#f6f6f6',
             line='#cccccc',linew=1,activeline='#cccccc',
                           *arg,**kw)

    def add_checkbutton(self,pos,*arg,**kw):
        return self.ui.add_checkbutton(pos,
            fontfg='#1a1a1a',fg='#868686',bg='#ededed',
                  activefg='#868686',activebg='#e5e5e5',
                  onfg='white',onbg='#334ac0',
                                *arg,**kw)

    def add_label(self,pos,*arg,**kw):
        return self.ui.add_label(pos,fg='#1a1a1a',bg='#f3f3f3',
                                 outline='#f3f3f3',*arg,**kw)

    def add_entry(self,pos,*arg,**kw):
        return self.ui.add_entry(pos,fg='#606060',bg='#fbfbfb',
            activefg='black',activebg='#fbfbfb',
            linew=2,outline='#868686',onoutline='#3041d8',
                          *arg,**kw)

    def add_separate(self,pos,*arg,**kw):
        return self.ui.add_separate(pos,fg='#e5e5e5',
                             *arg,**kw)

    def add_radiobutton(self,pos,*arg,**kw):
        return self.ui.add_radiobutton(pos,
                  fg='black',bg='white',
                  activefg='white',activebg='#4453db',
                                *arg,**kw)

    def add_link(self,pos,*arg,**kw):
        return self.ui.add_link(pos,fg='#4f62ca',
           activefg='red',activebg='#eaeaea',
                                *arg,**kw)

    def add_waitbar1(self,pos,*arg,**kw):
        return self.ui.add_waitbar1(pos,fg='#3041d8',
                                    bg='#f3f3f3',okfg='#3041d8',bd=5,
                                   *arg,**kw)

    def add_labelframe(self,uids:tuple,*arg,**kw):
        return self.ui.add_labelframe(uids,fg='#1a1a1a',bg='#f4f4f4',
                                      *arg,**kw)

    def add_waitbar2(self,pos,*arg,**kw):
        return self.ui.add_waitbar2(pos,
            fg='#334ac0',bg='#f3f3f3',okcolor='#3041d8',
                                    *arg,**kw)

    def add_combobox(self,pos,*arg,**kw):
        return self.ui.add_combobox(pos,
               fg='#1a1a1a',bg='#fbfbfb',
               activefg='#1a1a1a',activebg='#ededee',
                                    *arg,**kw)

    def add_progressbar(self,pos,*arg,**kw):
        return self.ui.add_progressbar(pos,
            fg='#868686',bg='#334ac0',back='#f3f3f3',
                  fontc='#79b8f8',*arg,**kw)

    def add_table(self,pos,*arg,**kw):
        return self.ui.add_table(pos,
                outline='#dadad8',fg='black',bg='white',
                headbg='#f4f4f2',*arg,**kw)

    def add_onoff(self,pos,*arg,**kw):
        return self.ui.add_onoff(pos,
                fg='#5a5a5a',bg='#ededed',
                onfg='#ffffff',onbg='#4453db',
                                 *arg,**kw)

    def add_spinbox(self,pos,*arg,**kw):
        return self.ui.add_spinbox(pos,
              fg='#1b1b1b',bg='#ffffff',line='#e5e5e5',
              activefg='#818181',activebg='#f2f2f2',
                                   *arg,**kw)

    def add_scalebar(self,pos,*arg,**kw):
        return self.ui.add_scalebar(pos,
            fg='#3b50ba',bg='#868686',activefg='#3b50ba',
            buttonbg='#ffffff',buttonoutline='#cccccc',
                                    *arg,**kw)

    def add_info(self,pos,*arg,**kw):
        return self.ui.add_info(pos,
           fg='#0078d4',bg='#f9f9f9',info_fg='#1a1a1a',
                                *arg,**kw)

    def add_menubar(self,uid,*arg,**kw):
        return self.ui.add_menubar(uid,
            fg='#1a1a1a',bg='#faf8f9',
            activefg='#1a1a1a',activebg='#efefef',*arg,**kw)

    def add_tooltip(self,uid,*arg,**kw):
        return self.ui.add_tooltip(uid,fg='#1a1a1a',bg='#efefef',
                                   *arg,**kw)

    def add_waitbar3(self,pos,*arg,**kw):
        return self.ui.add_waitbar3(pos,
            fg='#3041d8',bg='#f3f3f3',okcolor='#3041d8',
                                    *arg,**kw)

    def add_textbox(self,pos,*arg,**kw):
        return self.ui.add_textbox(pos,fg='#1a1a1a',bg='white',
              outline='#868686',onoutline='#3041d8',
                                   *arg,**kw)

    def add_scrollbar(self,pos,widget,*arg,**kw):
        return self.ui.add_scrollbar(pos,widget,
                bg='#f9f9f9',color='#8d8d8d',
                 oncolor='#8a8a8a',*arg,**kw)

    def add_listbox(self,pos,*arg,**kw):
        return self.ui.add_listbox(pos,
                bg='#f2f2f2',fg='black',activebg='#e9e9e9',sel='#b4bbea',
                                   *arg,**kw)

    def add_canvas(self,pos,*arg,**kw):
        return self.ui.add_canvas(pos,
                outline='#808080',linew=1,
                                  *arg,**kw)

    def add_pipspager(self,pos,*arg,**kw):
        return self.ui.add_pipspager(pos,
                bg='#f3f3f3',fg='#868686',buttonbg='#fafafa',
                                     *arg,**kw)

    def add_notebook(self,pos,*arg,**kw):
        return self.ui.add_notebook(pos,
                color='#f3f3f3',fg='#5d5d5d',bg='#f3f3f3',
                activefg='#595959',activebg='#eaeaea',
                onfg='#1a1a1a',onbg='#f9f9f9',
                                    *arg,**kw)

    def add_radiobox(self,pos,*arg,**kw):
        return self.ui.add_radiobox(pos,
                fontfg='black',fg='#8b8b8b',bg='#ededed',
                activefg='#898989',activebg='#e5e5e5',
                onfg='#3041d8',onbg='#ffffff',
                                    *arg,**kw)

    def add_ratingbar(self,pos,*arg,**kw):
        return self.ui.add_ratingbar(pos,
                fg='#5d5d5d',bg='#f3f3f3',
                onfg='#3041d8',onbg='#3041d8',
                                     *arg,**kw)

    def add_notecard(self,pos,*arg,**kw):
        return self.ui.add_notecard(pos,
                tfg='#1b1b1b',tbg='#fbfbfb',fg='#1a1a1a',
                bg='#f4f4f4',sep='#e5e5e5',
                                    *arg,**kw)

    def add_pivot(self,pos,*arg,**kw):
        return self.ui.add_pivot(pos,
                fg='#616161',bg='',
                activefg='#000000',activecolor='#5969e0',
                                 *arg,**kw)

    def add_button2(self,pos,*arg,**kw):
        return self.ui.add_button2(pos,fg='#1b1b1b',bg='#fbfbfb',
             activefg='#1a1a1a',activebg='#f6f6f6',
             line='#cccccc',linew=1,activeline='#cccccc',
                           *arg,**kw)

    def add_expander(self,pos,*arg,**kw):
        return self.ui.add_expander(pos,
                tfg='#1b1b1b',tbg='#fbfbfb',
                bg='#f4f4f4',sep='#e5e5e5',
                                    *arg,**kw)

    def add_waitframe(self,pos,*arg,**kw):
        return self.ui.add_waitframe(pos,
                fg='#fbfbfb',bg='#f6f6f6',
                                     *arg,**kw)

    def add_listview(self,pos,*arg,**kw):
        return self.ui.add_listview(pos,
                bg='#f3f3f3',activebg='#eaeaea',oncolor='#3041d8',
                scrobg='#f8f8f8',scroc='#868686',scrooc='#898989',
                                    *arg,**kw)

    def add_treeview(self,pos,*arg,**kw):
        return self.ui.add_treeview(pos,
                fg='#1a1a1a',bg='#f3f3f3',
                onfg='#1a1a1a',onbg='#eaeaea',
                oncolor='#3041d8',signcolor='#8a8a8a',
                *arg,**kw)

    def add_togglebutton(self,pos,*arg,**kw):
        return self.ui.add_togglebutton(pos,
                fg='#1b1b1b',bg='#fbfbfb',line='#cccccc',
                activefg='#f3f4fd',activebg='#3041d8',activeline='#5360de',
                *arg,**kw)
