![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RaiseNameChanged Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6947.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [ExecutableNodeBase Class](topic6938.md) : RaiseNameChanged Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_oldName_
    The name before it was changed.

_newName_
    The new name.

Glossary Item Box

Raises the [NameChanged](topic6979.md) event. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub RaiseNameChanged( _
       ByVal _oldName_ As String, _
       ByVal _newName_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ExecutableNodeBase](topic6938.md)
    Dim oldName As String
    Dim newName As String
     
    instance.RaiseNameChanged(oldName, newName)  
  
C#|   
---|---  
      
    
    protected void RaiseNameChanged( 
       string _oldName_ ,
       string _newName_
    )  
  
#### Parameters

 _oldName_
    The name before it was changed.
_newName_
    The new name.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ExecutableNodeBase Class](topic6938.md)   
[ExecutableNodeBase Members](topic6939.md)

©2024 DriveWorks Ltd. All Rights Reserved.
