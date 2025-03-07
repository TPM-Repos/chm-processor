Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Cancel Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationForm Class](topic11402.md) : Cancel Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Confirms the current active dialog. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Cancel()   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationForm](topic11402.md)
     
    instance.Cancel()  
  
C#|   
---|---  
      
    
    public void Cancel()  
  
# Exceptions

Exception| Description  
---|---  
System.InvalidOperationException| A specification is not running, or no dialog is active, or the dialog does no support closing in this way.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationForm Class](topic11402.md)   
[SpecificationForm Members](topic11403.md)


