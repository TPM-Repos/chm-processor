       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetSelection Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1140.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ViewControl Class](topic1119.md) : SetSelection Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newSelection_
    The new selection.

_clone_
    Dictates whether the array is cloned, if you make any changes to the array after calling this method, you should opt to clone the array, otherwise it is safe to pass false for this parameter's argument.

Glossary Item Box

Sets the current selection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub SetSelection( _
       ByVal _newSelection_() As Object, _
       ByVal _clone_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ViewControl](topic1119.md)
    Dim newSelection() As Object
    Dim clone As Boolean
     
    instance.SetSelection(newSelection, clone)  
  
C#|   
---|---  
      
    
    protected void SetSelection( 
       object[] _newSelection_ ,
       bool _clone_
    )  
  
#### Parameters

 _newSelection_
    The new selection.
_clone_
    Dictates whether the array is cloned, if you make any changes to the array after calling this method, you should opt to clone the array, otherwise it is safe to pass false for this parameter's argument.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ViewControl Class](topic1119.md)   
[ViewControl Members](topic1120.md)

©2024 DriveWorks Ltd. All Rights Reserved.
