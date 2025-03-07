_T_
    The type of the condition to add (Must inherit from [ComponentTaskCondition](topic6493.md)).

Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add<T>(String,Int32) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskConditions Class](topic6561.md) > [Add Method](topic6568.md) : Add<T>(String,Int32) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_title_
    The title of the condition to create.

_index_
    The index to insert the newly condition at.

Glossary Item Box

Creates and adds a new condition of the specified type to the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Add(Of T As [IComponentTaskCondition](topic6399.md))( _
       ByVal _title_ As String, _
       ByVal _index_ As Integer _
    ) As [ComponentTaskCondition](topic6493.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskConditions](topic6561.md)
    Dim title As String
    Dim index As Integer
    Dim value As [ComponentTaskCondition](topic6493.md)
     
    value = instance.Add(Of T)(title, index)  
  
C#|   
---|---  
      
    
    public [ComponentTaskCondition](topic6493.md) Add<T>( 
       string _title_ ,
       int _index_
    )
    where T: [IComponentTaskCondition](topic6399.md)  
  
#### Parameters

 _title_
    The title of the condition to create.
_index_
    The index to insert the newly condition at.

#### Type Parameters

_T_
    The type of the condition to add (Must inherit from [ComponentTaskCondition](topic6493.md)).

#### Return Value

The newly created condition.

# Exceptions

Exception| Description  
---|---  
System.ArgumentException| The specified type is not a valid [ComponentTaskCondition](topic6493.md) type.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskConditions Class](topic6561.md)   
[ComponentTaskConditions Members](topic6562.md)   
[Overload List](topic6568.md)


