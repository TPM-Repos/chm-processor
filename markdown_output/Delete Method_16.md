Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Delete Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectVariableCategory Class](topic4983.md) : Delete Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Deletes an empty project category. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Delete()   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectVariableCategory](topic4983.md)
     
    instance.Delete()  
  
C#|   
---|---  
      
    
    public void Delete()  
  
# Exceptions

Exception| Description  
---|---  
System.InvalidOperationException| Thrown if the project category contains any child categories or items.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectVariableCategory Class](topic4983.md)   
[ProjectVariableCategory Members](topic4984.md)


