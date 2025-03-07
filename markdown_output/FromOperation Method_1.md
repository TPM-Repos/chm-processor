Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FromOperation Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [TaskSequenceRef Class](topic13159.md) : FromOperation Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_operation_
    The operation for which to construct the reference.

Glossary Item Box

Constructs a task sequence reference for the given operation. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function FromOperation( _
       ByVal _operation_ As [Operation](topic11068.md) _
    ) As [TaskSequenceRef](topic13159.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim operation As [Operation](topic11068.md)
    Dim value As [TaskSequenceRef](topic13159.md)
     
    value = [TaskSequenceRef](topic13159.md).FromOperation(operation)  
  
C#|   
---|---  
      
    
    public static [TaskSequenceRef](topic13159.md) FromOperation( 
       [Operation](topic11068.md) _operation_
    )  
  
#### Parameters

 _operation_
    The operation for which to construct the reference.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TaskSequenceRef Class](topic13159.md)   
[TaskSequenceRef Members](topic13160.md)


