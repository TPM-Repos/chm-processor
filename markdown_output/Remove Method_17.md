Remove Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedDimensionCollection Class](topic14838.md) : Remove Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_dimension_
    The dimension to remove from the collection.

Glossary Item Box

Removes the given dimension from the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Remove( _
       ByVal _dimension_ As [ReleasedDimension](topic14826.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedDimensionCollection](topic14838.md)
    Dim dimension As [ReleasedDimension](topic14826.md)
    Dim value As Boolean
     
    value = instance.Remove(dimension)  
  
C#|   
---|---  
      
    
    public bool Remove( 
       [ReleasedDimension](topic14826.md) _dimension_
    )  
  
#### Parameters

 _dimension_
    The dimension to remove from the collection.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedDimensionCollection Class](topic14838.md)   
[ReleasedDimensionCollection Members](topic14839.md)


