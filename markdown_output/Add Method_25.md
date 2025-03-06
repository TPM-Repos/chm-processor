![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedViewCollection Class](topic15057.md) : Add Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sheetName_
    

_name_
    

_isAttached_
    

_left_
    

_top_
    

_scaleNumerator_
    

_scaleDenominator_
    

Glossary Item Box

Adds a new view. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _sheetName_ As String, _
       ByVal _name_ As String, _
       ByVal _isAttached_ As Boolean, _
       ByVal _left_ As Double, _
       ByVal _top_ As Double, _
       ByVal _scaleNumerator_ As Double, _
       ByVal _scaleDenominator_ As Double _
    ) As [ReleasedView](topic15041.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ReleasedViewCollection](topic15057.md)
    Dim sheetName As String
    Dim name As String
    Dim isAttached As Boolean
    Dim left As Double
    Dim top As Double
    Dim scaleNumerator As Double
    Dim scaleDenominator As Double
    Dim value As [ReleasedView](topic15041.md)
     
    value = instance.Add(sheetName, name, isAttached, left, top, scaleNumerator, scaleDenominator)  
  
C#|   
---|---  
      
    
    public [ReleasedView](topic15041.md) Add( 
       string _sheetName_ ,
       string _name_ ,
       bool _isAttached_ ,
       double _left_ ,
       double _top_ ,
       double _scaleNumerator_ ,
       double _scaleDenominator_
    )  
  
#### Parameters

 _sheetName_
    
_name_
    
_isAttached_
    
_left_
    
_top_
    
_scaleNumerator_
    
_scaleDenominator_
    

#### Return Value

The newly created view.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReleasedViewCollection Class](topic15057.md)   
[ReleasedViewCollection Members](topic15058.md)


