Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DisplayName Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Abstractions Namespace](topic5939.md) > [IHasRule Interface](topic5947.md) : DisplayName Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets an identifier which uniquely identifies the rule. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property DisplayName As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IHasRule](topic5947.md)
    Dim value As String
     
    value = instance.DisplayName  
  
C#|   
---|---  
      
    
    string DisplayName {get;}  
  
# Exceptions

Exception| Description  
---|---  
System.NotSupportedException| The rule is not writable.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IHasRule Interface](topic5947.md)   
[IHasRule Members](topic5948.md)


