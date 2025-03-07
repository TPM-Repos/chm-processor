Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetMessages Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectMessages Class](topic4627.md) : GetMessages Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all the messages which exist in the project. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function GetMessages() As [ProjectMessage()](topic4601.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectMessages](topic4627.md)
    Dim value() As [ProjectMessage](topic4601.md)
     
    value = instance.GetMessages()  
  
C#|   
---|---  
      
    
    public abstract [ProjectMessage[]](topic4601.md) GetMessages()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectMessages Class](topic4627.md)   
[ProjectMessages Members](topic4628.md)


