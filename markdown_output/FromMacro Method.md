Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FromMacro Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ConditionSequenceRef Class](topic12852.md) : FromMacro Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_macro_
    The macro for which to construct the reference.

Glossary Item Box

Constructs a condition sequence reference for the given specification macro. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function FromMacro( _
       ByVal _macro_ As [SpecificationMacro](topic11429.md) _
    ) As [ConditionSequenceRef](topic12852.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim macro As [SpecificationMacro](topic11429.md)
    Dim value As [ConditionSequenceRef](topic12852.md)
     
    value = [ConditionSequenceRef](topic12852.md).FromMacro(macro)  
  
C#|   
---|---  
      
    
    public static [ConditionSequenceRef](topic12852.md) FromMacro( 
       [SpecificationMacro](topic11429.md) _macro_
    )  
  
#### Parameters

 _macro_
    The macro for which to construct the reference.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConditionSequenceRef Class](topic12852.md)   
[ConditionSequenceRef Members](topic12853.md)


