checkboxs = """
MDFloatLayout:
    MDCheckbox:
        group: 'group'
        pos_hint: {"center_x": .6, "center_y": 0.8}
        size_hint: .1, .1
        on_active: app.check(*args)
        
    MDCheckbox:
        group: 'group'
        pos_hint: {"center_x": .6, "center_y": 0.7}
        size_hint: .1, .1
        on_active: app.check1(*args)
        
    MDCheckbox:
        group: 'group'
        pos_hint: {"center_x": .6, "center_y": 0.6}
        size_hint: .1, .1
        active: True
        on_active: app.check2(*args)
        
    MDCheckbox:
        group: 'group'
        pos_hint: {"center_x": .6, "center_y": 0.5}
        size_hint: .1, .1
        active: True
        on_active: app.check4(*args)
        
    MDCheckbox:
        group: 'group'
        pos_hint: {"center_x": .6, "center_y": 0.4}
        size_hint: .1, .1
        active: True
        on_active: app.check5(*args)
        
    MDCheckbox:
        group: 'group'
        pos_hint: {"center_x": .42, "center_y": 0.6}
        size_hint: .1, .1
        active: False
        on_active: app.check3(*args)
"""