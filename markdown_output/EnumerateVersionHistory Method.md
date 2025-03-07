Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EnumerateVersionHistory Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectVariable Class](topic4927.md) : EnumerateVersionHistory Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the version history for the variable. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function EnumerateVersionHistory() As IEnumerable(Of RuleVersionDetails)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectVariable](topic4927.md)
    Dim value As IEnumerable(Of RuleVersionDetails)
     
    value = instance.EnumerateVersionHistory()  
  
C#|   
---|---  
      
    
    public IEnumerable<RuleVersionDetails> EnumerateVersionHistory()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectVariable Class](topic4927.md)   
[ProjectVariable Members](topic4928.md)


