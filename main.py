def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    num_males = int(input('Enter the number of males in the class:'))
    num_females = int(input('Enter the number of females in the class:'))
    total_students = num_males + num_females

    m_perc = (num_males/total_students) *100
    f_perc = (num_females/total_students) *100

    print (f'Total number of students \t         {total_students}')
    print (f'The number of males and females \t {num_males}\t   {num_females}')
    print (f'The percentage of males and females \t {m_perc:.2f}\t   {f_perc:.2f}')
    #print (f'The percentage of males \t {m_perc:.2f}')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
