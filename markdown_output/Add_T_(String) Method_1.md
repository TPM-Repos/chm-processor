_T_
    The type of the condition to add (Must inherit from [ComponentTaskCondition](topic6493.md)).

Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add<T>(String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskConditions Class](topic6561.md) > [Add Method](topic6568.md) : Add<T>(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_title_
    The title of the condition to create.

Glossary Item Box

Creates and adds a new condition of the specified type to the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Add(Of T As [IComponentTaskCondition](topic6399.md))( _
       ByVal _title_ As String _
    ) As [ComponentTaskCondition](topic6493.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskConditions](topic6561.md)
    Dim title As String
    Dim value As [ComponentTaskCondition](topic6493.md)
     
    value = instance.Add(Of T)(title)  
  
C#|   
---|---  
      
    
    public [ComponentTaskCondition](topic6493.md) Add<T>( 
       string _title_
    )
    where T: [IComponentTaskCondition](topic6399.md)  
  
#### Parameters

 _title_
    The title of the condition to create.

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


