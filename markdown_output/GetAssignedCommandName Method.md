Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetAssignedCommandName Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IKeyboardShortcutService Interface](topic334.md) : GetAssignedCommandName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_keys_
    The key combination to check.

Glossary Item Box

Gets the name of the command assigned to the given key combination. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetAssignedCommandName( _
       ByVal _keys_ As Keys _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IKeyboardShortcutService](topic334.md)
    Dim keys As Keys
    Dim value As String
     
    value = instance.GetAssignedCommandName(keys)  
  
C#|   
---|---  
      
    
    string GetAssignedCommandName( 
       Keys _keys_
    )  
  
#### Parameters

 _keys_
    The key combination to check.

#### Return Value

The name of the command assigned to the given key combination, or a null reference of no assignment is registered.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IKeyboardShortcutService Interface](topic334.md)   
[IKeyboardShortcutService Members](topic335.md)


