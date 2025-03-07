Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedViewDimensionCollection Class](topic15078.md) : Add Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_address_
    

_distance_
    

_relativeTo_
    

Glossary Item Box

Adds a new dimension. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _address_ As String, _
       ByVal _distance_ As Double, _
       ByVal _relativeTo_ As [ViewDimensionRelativeTo](topic14030.md) _
    ) As [ReleasedViewDimension](topic15069.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedViewDimensionCollection](topic15078.md)
    Dim address As String
    Dim distance As Double
    Dim relativeTo As [ViewDimensionRelativeTo](topic14030.md)
    Dim value As [ReleasedViewDimension](topic15069.md)
     
    value = instance.Add(address, distance, relativeTo)  
  
C#|   
---|---  
      
    
    public [ReleasedViewDimension](topic15069.md) Add( 
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedViewDimensionCollection Class](topic15078.md)   
[ReleasedViewDimensionCollection Members](topic15079.md)


