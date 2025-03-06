       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
StateName Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) > [StoreSpecificationTask Class](topic12685.md) : StateName Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The name of the state to move the specification into for storage. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property StateName As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [StoreSpecificationTask](topic12685.md)
    Dim value As String
     
    instance.StateName = value
     
    value = instance.StateName  
  
C#|   
---|---  
      
    
    public string StateName {get; set;}  
  
# Remarks

Can be set to nothing, meaning that it will store the specification in the cancel state, if there is one.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[StoreSpecificationTask Class](topic12685.md)   
[StoreSpecificationTask Members](topic12686.md)


