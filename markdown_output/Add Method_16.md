Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _number_ As Integer, _
       ByVal _distance1_ As Double, _
       ByVal _distance2_ As Double _
    ) As [ReleasedBreakLine](topic14782.md)  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedBreakLineCollection Class](topic14792.md)   
[ReleasedBreakLineCollection Members](topic14793.md)


