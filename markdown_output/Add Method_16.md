![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic14798.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedBreakLineCollection Class](topic14792.md) : Add Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_number_
    The number of the break-line.

_distance1_
    The distance of the first line from the left/top edge of the view.

_distance2_
    The distance of the second line from the left/top edge of the view.

Glossary Item Box

Adds a new break-line. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _number_ As Integer, _
       ByVal _distance1_ As Double, _
       ByVal _distance2_ As Double _
    ) As [ReleasedBreakLine](topic14782.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ReleasedBreakLineCollection](topic14792.md)
    Dim number As Integer
    Dim distance1 As Double
    Dim distance2 As Double
    Dim value As [ReleasedBreakLine](topic14782.md)
     
    value = instance.Add(number, distance1, distance2)  
  
C#|   
---|---  
      
    
    public [ReleasedBreakLine](topic14782.md) Add( 
       int _number_ ,
       double _distance1_ ,
       double _distance2_
    )  
  
#### Parameters

 _number_
    The number of the break-line.
_distance1_
    The distance of the first line from the left/top edge of the view.
_distance2_
    The distance of the second line from the left/top edge of the view.

#### Return Value

The newly created break-line.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReleasedBreakLineCollection Class](topic14792.md)   
[ReleasedBreakLineCollection Members](topic14793.md)

©2024 DriveWorks Ltd. All Rights Reserved.
