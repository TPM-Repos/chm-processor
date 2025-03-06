![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedViewDimensionCollection Class](topic14384.md) : Add Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_address_
    

_distance_
    

_relativeTo_
    

Glossary Item Box

Adds a new dimension. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _address_ As String, _
       ByVal _distance_ As Double, _
       ByVal _relativeTo_ As [ViewDimensionRelativeTo](topic14030.md) _
    ) As [CapturedViewDimension](topic14374.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [CapturedViewDimensionCollection](topic14384.md)
    Dim address As String
    Dim distance As Double
    Dim relativeTo As [ViewDimensionRelativeTo](topic14030.md)
    Dim value As [CapturedViewDimension](topic14374.md)
     
    value = instance.Add(address, distance, relativeTo)  
  
C#|   
---|---  
      
    
    public [CapturedViewDimension](topic14374.md) Add( 
       string _address_ ,
       double _distance_ ,
       [ViewDimensionRelativeTo](topic14030.md) _relativeTo_
    )  
  
#### Parameters

 _address_
    
_distance_
    
_relativeTo_
    

#### Return Value

The newly created dimension.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[CapturedViewDimensionCollection Class](topic14384.md)   
[CapturedViewDimensionCollection Members](topic14385.md)


