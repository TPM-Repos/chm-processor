       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
StopSearch Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [NameSearchProcess Class](topic13195.md) : StopSearch Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Stops the searching process if it is running. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub StopSearch()   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [NameSearchProcess](topic13195.md)
     
    instance.StopSearch()  
  
C#|   
---|---  
      
    
    public void StopSearch()  
  
# Exceptions

Exception| Description  
---|---  
System.InvalidOperationException| Thrown when if this method is called when the process is not running.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[NameSearchProcess Class](topic13195.md)   
[NameSearchProcess Members](topic13196.md)


