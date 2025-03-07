Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Failures Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleasedEmail Class](topic5098.md) : Failures Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets information regarding the failed attempts at sending the email. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property Failures As IEnumerable(Of DeferredTaskFailureDetails)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedEmail](topic5098.md)
    Dim value As IEnumerable(Of DeferredTaskFailureDetails)
     
    value = instance.Failures  
  
C#|   
---|---  
      
    
    public IEnumerable<DeferredTaskFailureDetails> Failures {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedEmail Class](topic5098.md)   
[ReleasedEmail Members](topic5099.md)


