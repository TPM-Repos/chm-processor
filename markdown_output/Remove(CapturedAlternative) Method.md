       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Remove(CapturedAlternative) Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedAlternativeCollection Class](topic14039.md) > [Remove Method](topic14048.md) : Remove(CapturedAlternative) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_alternative_
    The alternative to remove from the collection.

Glossary Item Box

Removes the given alternative from the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Remove( _
       ByVal _alternative_ As [CapturedAlternative](topic14031.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedAlternativeCollection](topic14039.md)
    Dim alternative As [CapturedAlternative](topic14031.md)
    Dim value As Boolean
     
    value = instance.Remove(alternative)  
  
C#|   
---|---  
      
    
    public bool Remove( 
       [CapturedAlternative](topic14031.md) _alternative_
    )  
  
#### Parameters

 _alternative_
    The alternative to remove from the collection.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedAlternativeCollection Class](topic14039.md)   
[CapturedAlternativeCollection Members](topic14040.md)   
[Overload List](topic14048.md)


