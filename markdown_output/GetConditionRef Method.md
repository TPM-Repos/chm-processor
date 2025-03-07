Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetConditionRef Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ConditionSequenceRef Class](topic12852.md) : GetConditionRef Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_conditionIndex_
    The index of the condition in the sequence.

Glossary Item Box

Gets a reference to the specified condition. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetConditionRef( _
       ByVal _conditionIndex_ As Integer _
    ) As [ConditionRef](topic12843.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ConditionSequenceRef](topic12852.md)
    Dim conditionIndex As Integer
    Dim value As [ConditionRef](topic12843.md)
     
    value = instance.GetConditionRef(conditionIndex)  
  
C#|   
---|---  
      
    
    public [ConditionRef](topic12843.md) GetConditionRef( 
       int _conditionIndex_
    )  
  
#### Parameters

 _conditionIndex_
    The index of the condition in the sequence.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConditionSequenceRef Class](topic12852.md)   
[ConditionSequenceRef Members](topic12853.md)


