Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetVariables Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectVariableCategories Class](topic4966.md) : GetVariables Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all the variables which haven't been registered with a specific category. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetVariables() As [ProjectVariable()](topic4927.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectVariableCategories](topic4966.md)
    Dim value() As [ProjectVariable](topic4927.md)
     
    value = instance.GetVariables()  
  
C#|   
---|---  
      
    
    public [ProjectVariable[]](topic4927.md) GetVariables()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectVariableCategories Class](topic4966.md)   
[ProjectVariableCategories Members](topic4967.md)


