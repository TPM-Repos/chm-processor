Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterShortcut Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IKeyboardShortcutService Interface](topic334.md) : RegisterShortcut Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_keys_
    The keys that, when pressed, will invoke the given command.

_commandName_
    The name of the command to executed when the keyboard shortcut is pressed.

Glossary Item Box

Registers the given keyboard shortcut with the given command. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub RegisterShortcut( _
       ByVal _keys_ As Keys, _
       ByVal _commandName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IKeyboardShortcutService](topic334.md)
    Dim keys As Keys
    Dim commandName As String
     
    instance.RegisterShortcut(keys, commandName)  
  
C#|   
---|---  
      
    
    void RegisterShortcut( 
       Keys _keys_ ,
       string _commandName_
    )  
  
#### Parameters

 _keys_
    The keys that, when pressed, will invoke the given command.
_commandName_
    The name of the command to executed when the keyboard shortcut is pressed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IKeyboardShortcutService Interface](topic334.md)   
[IKeyboardShortcutService Members](topic335.md)


