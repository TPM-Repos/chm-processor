Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InvokeShortcut Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IKeyboardShortcutService Interface](topic334.md) : InvokeShortcut Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_keys_
    The shortcut keys that were pressed.

Glossary Item Box

Invokes whatever action is associated with the given shortcut keys. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function InvokeShortcut( _
       ByVal _keys_ As Keys _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IKeyboardShortcutService Interface](topic334.md)   
[IKeyboardShortcutService Members](topic335.md)


