_T_
    The type of the condition to add.

Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateCondition<T>(String,Double,Double) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Conditions Class](topic10865.md) > [CreateCondition Method](topic10872.md) : CreateCondition<T>(String,Double,Double) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_title_
    

_left_
    The left position of the condition.

_top_
    The top position of the condition.

Glossary Item Box

Creates and adds a new condition to the condition sequence. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateCondition(Of T As [Condition](topic10804.md))( _
       ByVal _title_ As String, _
       ByVal _left_ As Double, _
       ByVal _top_ As Double _
    ) As T  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Conditions](topic10865.md)
    Dim title As String
    Dim left As Double
    Dim top As Double
    Dim value As T
     
    value = instance.CreateCondition(Of T)(title, left, top)  
  
C#|   
---|---  
      
    
    public T CreateCondition<T>( 
       string _title_ ,
       double _left_ ,
       double _top_
    )
    where T: [Condition](topic10804.md)  
  
#### Parameters

 _title_
    
_left_
    The left position of the condition.
_top_
    The top position of the condition.

#### Type Parameters

_T_
    The type of the condition to add.

#### Return Value

The newly created condition.

# Exceptions

Exception| Description  
---|---  
System.ArgumentOutOfRangeException| The type specified in for the type parameter T isn't defined in a extension library.  
[DriveWorks.ItemExistsException](topic3561.md)| Thrown when a condition with the provided title already exists.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Conditions Class](topic10865.md)   
[Conditions Members](topic10866.md)   
[Overload List](topic10872.md)


