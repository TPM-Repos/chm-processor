Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetSuppressionContext Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Project Class](topic3859.md) : GetSuppressionContext Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Suppresses calculation and returns a disposable suppression context which can be used to resume calculation. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Function GetSuppressionContext() As IDisposable  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Project](topic3859.md)
    Dim value As IDisposable
     
    value = instance.GetSuppressionContext()  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public IDisposable GetSuppressionContext()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Project Class](topic3859.md)   
[Project Members](topic3860.md)


