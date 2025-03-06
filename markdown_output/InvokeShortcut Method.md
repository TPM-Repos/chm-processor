![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InvokeShortcut Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic340.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IKeyboardShortcutService Interface](topic334.md) : InvokeShortcut Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_keys_
    The shortcut keys that were pressed.

Glossary Item Box

Invokes whatever action is associated with the given shortcut keys. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function InvokeShortcut( _
       ByVal _keys_ As Keys _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IKeyboardShortcutService](topic334.md)
    Dim keys As Keys
    Dim value As Boolean
     
    value = instance.InvokeShortcut(keys)  
  
C#|   
---|---  
      
    
    bool InvokeShortcut( 
       Keys _keys_
    )  
  
#### Parameters

 _keys_
    The shortcut keys that were pressed.

#### Return Value

True if an action is associated with the given shortcut keys and executed.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IKeyboardShortcutService Interface](topic334.md)   
[IKeyboardShortcutService Members](topic335.md)

©2024 DriveWorks Ltd. All Rights Reserved.
