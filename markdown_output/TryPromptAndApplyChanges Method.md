       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryPromptAndApplyChanges Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IPendingChangesService Interface](topic355.md) : TryPromptAndApplyChanges Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_showCancelOption_
    

Glossary Item Box

If there are pending changes, a message will be displayed to the user asking if they want to apply them, then apply changes if they wish to. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function TryPromptAndApplyChanges( _
       ByVal _showCancelOption_ As Boolean _
    ) As [PromptAndApplyChangesResult](topic660.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IPendingChangesService](topic355.md)
    Dim showCancelOption As Boolean
    Dim value As [PromptAndApplyChangesResult](topic660.md)
     
    value = instance.TryPromptAndApplyChanges(showCancelOption)  
  
C#|   
---|---  
      
    
    [PromptAndApplyChangesResult](topic660.md) TryPromptAndApplyChanges( 
       bool _showCancelOption_
    )  
  
#### Parameters

 _showCancelOption_
    

#### Return Value

The result of the prompt and apply dialog, result is None if there were no changes.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IPendingChangesService Interface](topic355.md)   
[IPendingChangesService Members](topic356.md)


