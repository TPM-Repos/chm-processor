Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateCondition(Type,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Conditions Class](topic10865.md) > [CreateCondition Method](topic10872.md) : CreateCondition(Type,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_conditionType_
    The type of the condition to add.

_title_
    

Glossary Item Box

Creates and adds a new condition to the condition sequence. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateCondition( _
       ByVal _conditionType_ As Type, _
       ByVal _title_ As String _
    ) As [Condition](topic10804.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Conditions](topic10865.md)
    Dim conditionType As Type
    Dim title As String
    Dim value As [Condition](topic10804.md)
     
    value = instance.CreateCondition(conditionType, title)  
  
C#|   
---|---  
      
    
    public [Condition](topic10804.md) CreateCondition( 
       Type _conditionType_ ,
       string _title_
    )  
  
#### Parameters

 _conditionType_
    The type of the condition to add.
_title_
    

#### Return Value

The newly created condition.

# Exceptions

Exception| Description  
---|---  
System.ArgumentOutOfRangeException| The type specified in conditionType does not inherit from [Condition](topic10804.md) or isn't defined in a extension library.  
[DriveWorks.ItemExistsException](topic3561.md)| Thrown when a condition with the provided title already exists.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Conditions Class](topic10865.md)   
[Conditions Members](topic10866.md)   
[Overload List](topic10872.md)


