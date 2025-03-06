![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetOutputEndpoint Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10814.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Condition Class](topic10804.md) : TryGetOutputEndpoint Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the end point to find.

_isNavigation_
    True if the requested end point is a navigation end point.

_output_
    The end point (if found), otherwise a null reference.

Glossary Item Box

Attempts to retrieve the end point with the given name. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides Function TryGetOutputEndpoint( _
       ByVal _name_ As String, _
       ByVal _isNavigation_ As Boolean, _
       ByRef _output_ As [NodeOutput](topic7074.md) _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Condition](topic10804.md)
    Dim name As String
    Dim isNavigation As Boolean
    Dim output As [NodeOutput](topic7074.md)
    Dim value As Boolean
     
    value = instance.TryGetOutputEndpoint(name, isNavigation, output)  
  
C#|   
---|---  
      
    
    public override bool TryGetOutputEndpoint( 
       string _name_ ,
       bool _isNavigation_ ,
       ref [NodeOutput](topic7074.md) _output_
    )  
  
#### Parameters

 _name_
    The name of the end point to find.
_isNavigation_
    True if the requested end point is a navigation end point.
_output_
    The end point (if found), otherwise a null reference.

#### Return Value

True if the end point was found, otherwise false.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Condition Class](topic10804.md)   
[Condition Members](topic10805.md)

©2024 DriveWorks Ltd. All Rights Reserved.
