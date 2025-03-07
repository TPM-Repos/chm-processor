Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddGroup Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IViewCommandBarManager Interface](topic543.md) : AddGroup Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_title_
    The localized title of the group.

Glossary Item Box

Creates a new group which will contain related command buttons. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function AddGroup( _
       ByVal _title_ As String _
    ) As [ICommandBarGroup](topic99.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IViewCommandBarManager](topic543.md)
    Dim title As String
    Dim value As [ICommandBarGroup](topic99.md)
     
    value = instance.AddGroup(title)  
  
C#|   
---|---  
      
    
    [ICommandBarGroup](topic99.md) AddGroup( 
       string _title_
    )  
  
#### Parameters

 _title_
    The localized title of the group.

# Remarks

Groups created by this method are implicitly locked to the view to which the command bar manager belongs.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IViewCommandBarManager Interface](topic543.md)   
[IViewCommandBarManager Members](topic544.md)


