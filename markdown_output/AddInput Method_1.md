![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddInput Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4074.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectChildSpecificationProjectDef Class](topic4067.md) : AddInput Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_constantName_
    The constant name to bind.

Glossary Item Box

Adds a new input binging to this project definition. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function AddInput( _
       ByVal _constantName_ As String _
    ) As [ProjectChildSpecificationInputDef](topic4047.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationProjectDef](topic4067.md)
    Dim constantName As String
    Dim value As [ProjectChildSpecificationInputDef](topic4047.md)
     
    value = instance.AddInput(constantName)  
  
C#|   
---|---  
      
    
    public [ProjectChildSpecificationInputDef](topic4047.md) AddInput( 
       string _constantName_
    )  
  
#### Parameters

 _constantName_
    The constant name to bind.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectChildSpecificationProjectDef Class](topic4067.md)   
[ProjectChildSpecificationProjectDef Members](topic4068.md)

©2024 DriveWorks Ltd. All Rights Reserved.
