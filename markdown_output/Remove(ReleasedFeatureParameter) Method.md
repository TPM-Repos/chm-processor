       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Remove(ReleasedFeatureParameter) Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedFeatureParameterCollection Class](topic14911.md) > [Remove Method](topic14919.md) : Remove(ReleasedFeatureParameter) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_parameter_
    The parameter to remove from the collection.

Glossary Item Box

Removes the given parameter from the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Remove( _
       ByVal _parameter_ As [ReleasedFeatureParameter](topic14903.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedFeatureParameterCollection](topic14911.md)
    Dim parameter As [ReleasedFeatureParameter](topic14903.md)
    Dim value As Boolean
     
    value = instance.Remove(parameter)  
  
C#|   
---|---  
      
    
    public bool Remove( 
       [ReleasedFeatureParameter](topic14903.md) _parameter_
    )  
  
#### Parameters

 _parameter_
    The parameter to remove from the collection.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedFeatureParameterCollection Class](topic14911.md)   
[ReleasedFeatureParameterCollection Members](topic14912.md)   
[Overload List](topic14919.md)


