Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PriorityTags Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [JobRequestTagInformation Class](topic3604.md) : PriorityTags Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the tags that must be processed first. The order of the collection determines the priority. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property PriorityTags As String()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [JobRequestTagInformation](topic3604.md)
    Dim value() As String
     
    value = instance.PriorityTags  
  
C#|   
---|---  
      
    
    public string[] PriorityTags {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[JobRequestTagInformation Class](topic3604.md)   
[JobRequestTagInformation Members](topic3605.md)


