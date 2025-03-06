       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Remove(CapturedDimension) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic14173.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedDimensionCollection Class](topic14162.md) > [Remove Method](topic14171.md) : Remove(CapturedDimension) Method  
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
      
    
    Public Overloads Function Remove( _
       ByVal _dimension_ As [CapturedDimension](topic14154.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedDimensionCollection](topic14162.md)
    Dim dimension As [CapturedDimension](topic14154.md)
    Dim value As Boolean
     
    value = instance.Remove(dimension)  
  
C#|   
---|---  
      
    
    public bool Remove( 
       [CapturedDimension](topic14154.md) _dimension_
    )  
  
#### Parameters

 _dimension_
    The dimension to remove from the collection.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedDimensionCollection Class](topic14162.md)   
[CapturedDimensionCollection Members](topic14163.md)   
[Overload List](topic14171.md)

©2024 DriveWorks Ltd. All Rights Reserved.
