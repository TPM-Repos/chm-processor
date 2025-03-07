Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTransition Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Transitions Class](topic11787.md) : CreateTransition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The unique name of the transition.

Glossary Item Box

Creates and returns a new transition. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTransition( _
       ByVal _name_ As String _
    ) As [Transition](topic11757.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Transitions](topic11787.md)
    Dim name As String
    Dim value As [Transition](topic11757.md)
     
    value = instance.CreateTransition(name)  
  
C#|   
---|---  
      
    
    public [Transition](topic11757.md) CreateTransition( 
       string _name_
    )  
  
#### Parameters

 _name_
    The unique name of the transition.

#### Return Value

A new instance of the [Transition](topic11757.md) class.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Transitions Class](topic11787.md)   
[Transitions Members](topic11788.md)


