Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConstantEventArgs Constructor(ProjectConstant)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ConstantEventArgs Class](topic2595.md) > [ConstantEventArgs Constructor](topic2601.md) : ConstantEventArgs Constructor(ProjectConstant)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_constant_
    The constant that was changed.

Glossary Item Box

Initializes a new instance of the [ConstantEventArgs](topic2595.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _constant_ As [ProjectConstant](topic4171.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim constant As [ProjectConstant](topic4171.md)
     
    Dim instance As New [ConstantEventArgs](topic2595.md)(constant)  
  
C#|   
---|---  
      
    
    public ConstantEventArgs( 
       [ProjectConstant](topic4171.md) _constant_
    )  
  
#### Parameters

 _constant_
    The constant that was changed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConstantEventArgs Class](topic2595.md)   
[ConstantEventArgs Members](topic2596.md)   
[Overload List](topic2601.md)


