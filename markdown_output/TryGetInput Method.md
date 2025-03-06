![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetInput Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4081.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectChildSpecificationProjectDef Class](topic4067.md) : TryGetInput Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_constantName_
    Name of the constant to get the input for.

_input_
    The input to be set.

Glossary Item Box

Attempts to get a specified input from the given constant name. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetInput( _
       ByVal _constantName_ As String, _
       ByRef _input_ As [ProjectChildSpecificationInputDef](topic4047.md) _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationProjectDef](topic4067.md)
    Dim constantName As String
    Dim input As [ProjectChildSpecificationInputDef](topic4047.md)
    Dim value As Boolean
     
    value = instance.TryGetInput(constantName, input)  
  
C#|   
---|---  
      
    
    public bool TryGetInput( 
       string _constantName_ ,
       ref [ProjectChildSpecificationInputDef](topic4047.md) _input_
    )  
  
#### Parameters

 _constantName_
    Name of the constant to get the input for.
_input_
    The input to be set.

#### Return Value

True if the input was found.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectChildSpecificationProjectDef Class](topic4067.md)   
[ProjectChildSpecificationProjectDef Members](topic4068.md)

©2024 DriveWorks Ltd. All Rights Reserved.
