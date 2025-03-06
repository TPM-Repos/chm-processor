![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Rename Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7565.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ChildSpecificationList Class](topic7547.md) : Rename Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newName_
    The new name of the control.

Glossary Item Box

Renames the control. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides Sub Rename( _
       ByVal _newName_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ChildSpecificationList](topic7547.md)
    Dim newName As String
     
    instance.Rename(newName)  
  
C#|   
---|---  
      
    
    public override void Rename( 
       string _newName_
    )  
  
#### Parameters

 _newName_
    The new name of the control.

# ![](dotnetimages/collapse.gif)Remarks

References to the renamed control are not refactored, to refactor them, use the [ControlBase.CreateRefactorProcess](topic7706.md) method.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ChildSpecificationList Class](topic7547.md)   
[ChildSpecificationList Members](topic7548.md)

©2024 DriveWorks Ltd. All Rights Reserved.
