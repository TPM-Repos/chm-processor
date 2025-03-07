Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetVariables Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectVariables Class](topic5010.md) : GetVariables Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all the variables which exist in the project. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function GetVariables() As [ProjectVariable()](topic4927.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectVariables](topic5010.md)
    Dim value() As [ProjectVariable](topic4927.md)
     
    value = instance.GetVariables()  
  
C#|   
---|---  
      
    
    public abstract [ProjectVariable[]](topic4927.md) GetVariables()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectVariables Class](topic5010.md)   
[ProjectVariables Members](topic5011.md)


