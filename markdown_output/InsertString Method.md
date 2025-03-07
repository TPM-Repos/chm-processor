Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InsertString Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.RulesBuilder Namespace](topic1581.md) > [IRuleWindow Interface](topic1607.md) : InsertString Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The value to insert.

Glossary Item Box

Inserts specified value into either the active rule's formula or the currently active wizard. While ensuring that it is wrapped in string quotes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub InsertString( _
       ByVal _value_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IRuleWindow](topic1607.md)
    Dim value As String
     
    instance.InsertString(value)  
  
C#|   
---|---  
      
    
    void InsertString( 
       string _value_
    )  
  
#### Parameters

 _value_
    The value to insert.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IRuleWindow Interface](topic1607.md)   
[IRuleWindow Members](topic1608.md)


