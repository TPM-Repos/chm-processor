Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FromMacro Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [TaskSequenceRef Class](topic13159.md) : FromMacro Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_macro_
    The macro for which to construct the reference.

Glossary Item Box

Constructs a task sequence reference for the given macro. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function FromMacro( _
       ByVal _macro_ As [SpecificationMacro](topic11429.md) _
    ) As [TaskSequenceRef](topic13159.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim macro As [SpecificationMacro](topic11429.md)
    Dim value As [TaskSequenceRef](topic13159.md)
     
    value = [TaskSequenceRef](topic13159.md).FromMacro(macro)  
  
C#|   
---|---  
      
    
    public static [TaskSequenceRef](topic13159.md) FromMacro( 
       [SpecificationMacro](topic11429.md) _macro_
    )  
  
#### Parameters

 _macro_
    The macro for which to construct the reference.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TaskSequenceRef Class](topic13159.md)   
[TaskSequenceRef Members](topic13160.md)


