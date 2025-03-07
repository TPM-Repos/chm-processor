Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FromOperation Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ConditionSequenceRef Class](topic12852.md) : FromOperation Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_operation_
    The operation for which to construct the reference.

Glossary Item Box

Constructs a condition sequence reference for the given operation. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function FromOperation( _
       ByVal _operation_ As [Operation](topic11068.md) _
    ) As [ConditionSequenceRef](topic12852.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim operation As [Operation](topic11068.md)
    Dim value As [ConditionSequenceRef](topic12852.md)
     
    value = [ConditionSequenceRef](topic12852.md).FromOperation(operation)  
  
C#|   
---|---  
      
    
    public static [ConditionSequenceRef](topic12852.md) FromOperation( 
       [Operation](topic11068.md) _operation_
    )  
  
#### Parameters

 _operation_
    The operation for which to construct the reference.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConditionSequenceRef Class](topic12852.md)   
[ConditionSequenceRef Members](topic12853.md)


