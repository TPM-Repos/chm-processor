       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetToleranceData Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedDimension Class](topic14826.md) : SetToleranceData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_type_
    The tolerance type.

_lower_
    The lower tolerance value.

_upper_
    The upper tolerance value.

Glossary Item Box

Sets the tolerance data for the dimension, creating it if it doesn't already exist. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SetToleranceData( _
       ByVal _type_ As Integer, _
       ByVal _lower_ As Double, _
       ByVal _upper_ As Double _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedDimension](topic14826.md)
    Dim type As Integer
    Dim lower As Double
    Dim upper As Double
     
    instance.SetToleranceData(type, lower, upper)  
  
C#|   
---|---  
      
    
    public void SetToleranceData( 
       int _type_ ,
       double _lower_ ,
       double _upper_
    )  
  
#### Parameters

 _type_
    The tolerance type.
_lower_
    The lower tolerance value.
_upper_
    The upper tolerance value.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedDimension Class](topic14826.md)   
[ReleasedDimension Members](topic14827.md)


