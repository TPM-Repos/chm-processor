![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic14982.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedLayerCollection Class](topic14976.md) : Add Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the layer to add.

_visibility_
    The value of the visibility parameter.

Glossary Item Box

Adds a new layer. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _name_ As String, _
       ByVal _visibility_ As String _
    ) As [ReleasedLayer](topic14968.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ReleasedLayerCollection](topic14976.md)
    Dim name As String
    Dim visibility As String
    Dim value As [ReleasedLayer](topic14968.md)
     
    value = instance.Add(name, visibility)  
  
C#|   
---|---  
      
    
    public [ReleasedLayer](topic14968.md) Add( 
       string _name_ ,
       string _visibility_
    )  
  
#### Parameters

 _name_
    The name of the layer to add.
_visibility_
    The value of the visibility parameter.

#### Return Value

The newly created layer.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReleasedLayerCollection Class](topic14976.md)   
[ReleasedLayerCollection Members](topic14977.md)

©2024 DriveWorks Ltd. All Rights Reserved.
