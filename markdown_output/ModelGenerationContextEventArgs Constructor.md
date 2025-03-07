Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ModelGenerationContextEventArgs Constructor   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [ModelGenerationContextEventArgs Class](topic15264.md) : ModelGenerationContextEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_context_
    The generation context.

Glossary Item Box

Initializes a new instance of the [ModelGenerationContextEventArgs](topic15264.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _context_ As [IModelGenerationContext](topic15157.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim context As [IModelGenerationContext](topic15157.md)
     
    Dim instance As New [ModelGenerationContextEventArgs](topic15264.md)(context)  
  
C#|   
---|---  
      
    
    public ModelGenerationContextEventArgs( 
       [IModelGenerationContext](topic15157.md) _context_
    )  
  
#### Parameters

 _context_
    The generation context.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ModelGenerationContextEventArgs Class](topic15264.md)   
[ModelGenerationContextEventArgs Members](topic15265.md)


