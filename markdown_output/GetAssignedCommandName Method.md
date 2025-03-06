![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetAssignedCommandName Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic339.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IKeyboardShortcutService Interface](topic334.md) : GetAssignedCommandName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_keys_
    The key combination to check.

Glossary Item Box

Gets the name of the command assigned to the given key combination. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetAssignedCommandName( _
       ByVal _keys_ As Keys _
    ) As String  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IKeyboardShortcutService Interface](topic334.md)   
[IKeyboardShortcutService Members](topic335.md)

©2024 DriveWorks Ltd. All Rights Reserved.
