Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTransition Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Transitions Class](topic11787.md) : GetTransition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the transition to get.

Glossary Item Box

Gets the transition with the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetTransition( _
       ByVal _name_ As String _
    ) As [Transition](topic11757.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Transitions](topic11787.md)
    Dim name As String
    Dim value As [Transition](topic11757.md)
     
    value = instance.GetTransition(name)  
  
C#|   
---|---  
      
    
    public [Transition](topic11757.md) GetTransition( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the transition to get.

#### Return Value

The transition with the specified name.

# Exceptions

Exception| Description  
---|---  
[DriveWorks.ItemNotFoundException](topic3571.md)| The transition could not be found.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Transitions Class](topic11787.md)   
[Transitions Members](topic11788.md)


